// src/types/index.ts
export interface PredictionResponse {
  classe: number;
  label: string;
  probabilidades: number[][];
}