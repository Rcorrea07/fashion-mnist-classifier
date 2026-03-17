// src/components/ProbabilityChart.tsx
import React from "react";
import { Bar } from "react-chartjs-2";
import { Chart as ChartJS, BarElement, CategoryScale, LinearScale, Tooltip, Legend } from "chart.js";
import type { PredictionResponse } from "../types";

ChartJS.register(BarElement, CategoryScale, LinearScale, Tooltip, Legend);

interface Props {
  result: PredictionResponse;
}

export default function ProbabilityChart({ result }: Props) {
  const labels = ["Camiseta", "Calça", "Pulôver", "Vestido", "Casaco", "Sandália", "Camisa", "Tênis", "Bolsa", "Bota"];

  const data = {
    labels: labels,
    datasets: [
      {
        label: "Confiança (%)",
        data: result.probabilidades[0].map((x: number) => x * 100),
        backgroundColor: "rgba(75, 192, 192, 0.5)",
        borderColor: "rgba(75, 192, 192, 1)",
        borderWidth: 1,
      },
    ],
  };

  const options = { responsive: true, scales: { y: { beginAtZero: true, max: 100 } } };

  return (
    <div className="result-card">
      <h3>Probabilidades</h3>
      <Bar data={data} options={options} />
    </div>
  );
}