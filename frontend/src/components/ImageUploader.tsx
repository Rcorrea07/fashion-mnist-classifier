import React from "react";

interface Props {
  image: File | null;
  setImage: (file: File | null) => void;
  onUpload: () => void;
}

export default function ImageUploader({ image, setImage, onUpload }: Props) {
  return (
    <div>
      <input
        type="file"
        accept="image/*"
        onChange={(e) => {
          if (e.target.files?.[0]) {
            setImage(e.target.files[0]);
          }
        }}
      />

      {image && (
        <div style={{ marginTop: 15 }}>
          <p>Pré-visualização:</p>
          <img
            src={URL.createObjectURL(image)}
            alt="preview"
            style={{ width: 150, height: "auto", border: "1px solid #ccc", padding: 5 }}
          />
        </div>
      )}

      <button onClick={onUpload} disabled={!image} style={{ marginTop: 20 }}>
        Enviar imagem
      </button>
    </div>
  );
}