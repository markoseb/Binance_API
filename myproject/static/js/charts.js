


var randomScalingFactor = function() {
        return (Math.random() > 0.5 ? 1.0 : -1.0) * Math.round(Math.random() * 100);
    };
    var randomColorFactor = function() {
        return Math.round(Math.random() * 255);
    };

    var barChartData = {
        labels: ["2", "3", "4", "5", "6", "7", "8"],

        datasets: [ {
            type: 'line',
            label: 'Dataset 3',
            backgroundColor: "rgba(43, 111, 106, 1)",
            data: [randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor()]
        }, ]

    };


    var optionsChart ={

            responsive: true,
            scales: {
                        xAxes: [{
                            display: true,
                            scaleLabel: {
                                display: true,
                                labelString: 'Date/Time',
                                fontColor:"white",
                                fontSize:15
                            },
                            ticks: {
                               fontColor: "white",
                               fontSize: 14
                              }
                        }],
                        yAxes: [{
                            display: true,
                            scaleLabel: {
                                display: true,
                                labelString: 'USDT',
                                fontColor: "white",
                                fontSize:15
                            },
                            ticks: {
                                  fontColor: "white",
                                  fontSize: 14
                            }
                        }]
                 }
         };
function ranodomData() {
        $.each(barChartData.datasets, function(i, dataset) {
            dataset.backgroundColor = 'rgba(' + randomColorFactor() + ',' + randomColorFactor() + ',' + randomColorFactor() + ',.7)';
            dataset.data = [randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor()];

        });
        myBar.update();
 }





var myBar = null;
var result_x = [];
var result_y = [];

function runChart(x,y)
{

    setData(x,y,update=false)

    var can = document.querySelector('canvas');
    can.style.position = 'absolute';

    can.style.left = "350px";

        var ctx =can.getContext("2d");
        myBar = new Chart(ctx, {
            type: 'bar',
            data: barChartData,
            options: optionsChart

        });
        result_x = [];
        result_y = [];


};



function setData(x,y,update=true) {

    for(var i in y)
        result_y.push(y[i]);
    for(var i in x)
        result_x.push(x[i]);

        $.each(barChartData.datasets, function(i, dataset) {
            dataset.data = result_y;
            dataset.label = document.getElementById("token").value;
            barChartData.labels=result_x;
        });
        $.each(optionsChart.scales.yAxes, function(i, yAxes) {
            yAxes.scaleLabel.labelString=document.getElementById("valuesType").value;
       });

        if (update==true){
        myBar.update();
        }
        result_x = [];
        result_y = [];
    }


