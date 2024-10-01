// Obtener datos desde la plantilla
const labels = [
    {% for day in days %}
    "{{ day.day }}",
    {% endfor %}
];

const data = {
    labels: labels,
    datasets: [{
        label: 'Money End',
        data: [
            {% for day in days %}
            {{ day.money_end }},
            {% endfor %}
        ],
        borderColor: 'rgba(75, 192, 192, 1)',
        backgroundColor: 'rgba(75, 192, 192, 0.2)',
        fill: true,
        tension: 0.1
    }]
};

// Configuración del gráfico
const config = {
    type: 'line',
    data: data,
    options: {
        responsive: true,
        scales: {
            x: {
                title: {
                    display: true,
                    text: 'Day'
                }
            },
            y: {
                title: {
                    display: true,
                    text: 'Money End'
                }
            }
        }
    }
};

// Renderizar el gráfico de línea en el canvas
const myChart = new Chart(
    document.getElementById('myChart'),
    config
);