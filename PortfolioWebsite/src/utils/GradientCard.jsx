// GradientCard.js
import React from "react";

function GradientCard({ title, description, colors }) {
  // Ensure colors array has at least 3 colors
  const gradientColors = colors.join(' ');

  return (
    <div className={`relative w-full h-full p-8 bg-gradient-to-br ${gradientColors} rounded-xl shadow-lg transform hover:scale-105 transition-transform duration-300 overflow-hidden`}>
      {/* Gradient shadow effect */}
      <div className="absolute inset-0 bg-gradient-to-br from-black/30 to-transparent rounded-xl"></div>
      <div className="relative z-10 text-white">
        <h1 className="text-3xl font-bold mb-2">{title}</h1>
        
        <ul className="text-xl mb-4 list-disc pl-5">
          {description.map((item, index) => (
            <li key={index}>{item}</li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default GradientCard;
