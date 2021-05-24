<script>
    import Chart from 'svelte-frappe-charts';
    import Heading from '../lib/Heading.svelte';
    import img from "/img/pieChart.png";
    import jsonArray from "/src/AppleStock.json";

    let dates = []
    let data = {
        labels: [],
        datasets: [
                {
                    values: []
                }
            ]
    };
    
    jsonArray.forEach(element => {
        data.labels.push(element["Date"])
        data.datasets[0].values.push(element["AAPL.Close"])
    });
    console.log(data)
</script>
<Heading>My Portfolio</Heading>

<div class="flex flex-col mx-auto">
    <img class="width:100%; height:auto" src={img} alt="background image" />
    <Chart
                {data}
                title="Apple Stock Prices"
                type="line"
                height={600}
                colors={['#0a66c2']}
                lineOptions={{
                    regionFill: 1,
                    xIsSeries: 10,
                    xAxisMode: "span",
                    spline: 1,
                    hideDots: 1
                }}
            />
</div>