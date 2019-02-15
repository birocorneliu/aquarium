const loadData = function(url) {
  return new Promise((resolve) => {
    const xhr = new XMLHttpRequest();

    xhr.open("GET", url);
    xhr.onload = () => {
      let data = {};

      if(xhr.status != 200) {
        data = {err: xhr.status};
      } else {
        try {
          data = JSON.parse(xhr.responseText);
        } catch(e) {
          data = {err: e}
        }
      }

      resolve(data)
    }

    xhr.send();
  })
}

const drawPlot = async function() {
  const data = await loadData("/get_temperatures");

  const trace1 = {
    x: [],
    y: [],
    mode: "lines",
    type: "scatter",
    line: {shape: 'spline'},
    name: "temperature"
  }

  data.forEach(({temperature, register_date}, i) => {
    trace1.x.push(register_date);
    trace1.y.push(temperature);
  })

  var layout = {
    xaxis: {
      type: 'date',
    },
    yaxis: {
      title: '°C'
    },
    title: ' ',
    plot_bgcolor: "#000",
    paper_bgcolor: "#000",
  };

  Plotly.newPlot("plot", [trace1], layout, {displayModeBar: false});


  setTimeout(drawPlot, 60 * 1000);
}

const clickHandler = async function(evt) {
  const cmd = evt.target.id;
  const action = evt.target.getAttribute("data-value") === "on" ? "close" : "open";

  evt.target.setAttribute("data-value", action === "close" ? "off" : "on");

  await loadData(`/pin/${cmd}/${action}`);

  createCommands();
}

const createCommands = async function() {
  const data = await loadData("/status");

  const commands = document.querySelector("#commands");

  Object.entries(data).forEach(([key, value]) => {
    let command = commands.querySelector(`#${key}`);

    if(!command) {
      command = document.createElement("button");
      command.id = key;
      command.innerHTML = key.replace("_", " ");

      command.addEventListener("click", clickHandler);

      commands.appendChild(command);
    }

    command.setAttribute("data-value", value ? "on" : "off")
  });
}


const initialize = function() {
  const resetBtn = document.querySelector("#reset");
  resetBtn.addEventListener("click", async () => {
    await loadData("/set_procedure/reset");

    createCommands();
  })


  createCommands();
  drawPlot();

  setInterval(createCommands, 10 * 1000);
};

initialize();
