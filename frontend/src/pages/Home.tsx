import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { uploadImage } from "../services/api";
import type { PredictionResponse } from "../types";
import ImageUploader from "../components/ImageUploader";
import PredictionResult from "../components/PredictionResult";
import ProbabilityChart from "../components/ProbabilityChart";

export default function Home() {
  const navigate = useNavigate();
  const [image, setImage] = useState<File | null>(null);
  const [result, setResult] = useState<PredictionResponse | null>(null);

  const handleUpload = async () => {
    if (!image) return;
    try {
      const data = await uploadImage(image);
      setResult(data);
    } catch (error) {
      console.error("Erro ao enviar a imagem:", error);
      alert("Erro ao conectar com a API. O backend está rodando?");
    }
  };

  return (
    <div className="container">
      <button onClick={() => navigate("/sobre")} style={{ marginBottom: 20 }}>
        Sobre o Projeto
      </button>

      <h1>Classificador Fashion MNIST</h1>

      <ImageUploader image={image} setImage={setImage} onUpload={handleUpload} />

      {result && <PredictionResult result={result} />}
      {result && <ProbabilityChart result={result} />}
    </div>
  );
}