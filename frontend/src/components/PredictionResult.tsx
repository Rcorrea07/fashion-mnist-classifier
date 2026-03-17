// src/components/PredictionResult.tsx
import React from "react";
import type { PredictionResponse } from "../types";

interface Props {
  result: PredictionResponse;
}

export default function PredictionResult({ result }: Props) {
  const confianca = (Math.max(...result.probabilidades[0]) * 100).toFixed(1);

  return (
    <div
      style={{
        marginTop: 20,
        padding: 15,
        borderRadius: 8,
        backgroundColor: "#f7f7f7",
        border: "1px solid #ddd",
        width: "fit-content"
      }}
    >
      <h3 style={{ margin: 0, marginBottom: 10 }}>Resultado</h3>
      <p style={{ margin: "5px 0" }}><strong>Classe prevista:</strong> {result.label}</p>
      <p style={{ margin: "5px 0" }}><strong>Confiança:</strong> {confianca}%</p>
    </div>
  );
}