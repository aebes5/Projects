import React from 'react'
import GradientCard from './GradientCard';

const SkillsCardView = () => {
  return (
    <div>
      <h_title>Technical Skills</h_title>
      <h_desc>A list of technical and more generalized skills.</h_desc>
      <div className="flex items-center justify-center">
      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6 p-4">
      <GradientCard
          title="Programming Languages"
          description={["Python", "C++", "C", "R"]}
          colors={["from-green-500", "via-teal-500", "to-blue-500"]}

        />
        <GradientCard
          title="Data Visualization"
          description={["Matplotlib", "Pandas"]}
          colors={["from-green-500", "via-teal-500", "to-blue-500"]}

        />
        <GradientCard
          title="Machine/Deep Learning"
          description={["Scikit-learn", "PyTorch"]}
          colors={["from-green-500", "via-teal-500", "to-blue-500"]}

        />
        <GradientCard
          title="Optimization"
          description={["Numerical Methods", "NumPy", "SciPy", "Pyomo"]}
          colors={["from-green-500", "via-teal-500", "to-blue-500"]}

        />
        <GradientCard
          title="Tools/Technologies"
          description={["Git", "Linux/Unix", "Intel MKL", "SQL"]}
          colors={["from-green-500", "via-teal-500", "to-blue-500"]}

        />
        <GradientCard
          title="Mathematics"
          description={[
            "Calculus",
            "Linear Algebra",
            "Differential Equations",
            "Probability and Statistics"
          ]}
          colors={["from-green-500", "via-teal-500", "to-blue-500"]}

        />

              </div>
      </div>
    </div>
  );
};


export default SkillsCardView



