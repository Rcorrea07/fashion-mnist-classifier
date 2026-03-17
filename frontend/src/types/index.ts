export interface PredictionResponse {
  classe: number;
  label: string;
  probabilidades: number[][];
}