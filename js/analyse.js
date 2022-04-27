var ctx1 = document.getElementById('chart1').getContext('2d');
var ctx2 = document.getElementById('chart2').getContext('2d');

var chart1 = new Chart(ctx1, {
    type: 'bar',
    data: {
        labels: ['Mineur', 'Moyen', 'Elevé', 'Très élevé'],
        datasets: [{
            label: "Nombre d'incidents par niveau",
            data: [25, 37, 47, 12],
            backgroundColor: [
                'yellow',
                'orange',
                'red',
                'black',
            ]
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});

var chart2 = new Chart(ctx2, {
    type: 'bar',
    data: {
        labels: ['Revêtement', 'Travaux', 'Circulation'],
        datasets: [{
            label: "Nombre d'incidents par catégorie",
            data: [47, 31, 9],
            backgroundColor: [
                'grey',
                'grey',
                'grey',
            ]
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});
