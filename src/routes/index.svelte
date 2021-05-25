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

    function exportCsv(){

    }
</script>
<Heading>My Portfolio</Heading>

<div class="flex flex-col p-4 mx-auto">
    <form method="get" action="/src/AppleStock.csv">
        <button class="bg-gray-300 hover:bg-gray-400 text-gray-800 font-bold w-max py-2 px-4 rounded inline-flex items-center" on:click={exportCsv()}>
            <svg class="fill-current w-4 h-4 mr-2" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20"><path d="M13 8V2H7v6H2l8 8 8-8h-5zM0 18h20v2H0v-2z"/></svg>
            <span>Export to CSV</span>
        </button>
    </form>
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