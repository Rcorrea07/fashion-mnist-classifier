import React from "react";
import { useNavigate } from "react-router-dom";

export default function About() {
  const navigate = useNavigate();

  return (
    <div className="container">
      <button onClick={() => navigate("/")} style={{ marginBottom: 20 }}>
        Voltar para a Home
      </button>
      
      <h1>Sobre o Projeto</h1>
      <p>Este sistema utiliza uma rede neural convolucional (CNN) treinada no dataset Fashion‑MNIST para classificar imagens em 10 categorias de roupas.</p>
      <p>O pipeline completo inclui:</p>
      <ul>
        <li>Frontend em React + TypeScript</li>
        <li>Backend em FastAPI</li>
        <li>Processamento de imagem com OpenCV</li>
        <li>Modelo TensorFlow em Python</li>
      </ul>
      <p>Futuras melhorias incluem: Transfer Learning, dataset real e interface aprimorada.</p>
    </div>
  );
}