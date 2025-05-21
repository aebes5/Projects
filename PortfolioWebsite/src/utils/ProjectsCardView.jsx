import React from "react";
import GradientCard from "./GradientCard"; 

const CardView = () => {
  return (
    <div>
      <h_title>School/Personal Projects</h_title>
      <h_desc>A list of school and personal projects I've worked on.</h_desc>
      <div className="flex items-center justify-center">
      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6 p-4">
        <GradientCard
          title="Portfolio Website"
          description={["Built this portfolio website using HTML, CSS, and JavaScript with React and Tailwind frameworks.",
              "Developed an understanding of front-end development given my limited exposure in university courses."]
          }
          colors={["from-red-500", "via-orange-500", "to-yellow-500"]}

        />
        
        <GradientCard
          title="Fitness Tracker Application"
          description={["Led a team of three to develop an Android application using Java.",
              "Managed version control using Git to ensure consistency across contributions.",
              "Facilitated team communication to meet all project deadlines."]
          }
          colors={["from-red-500", "via-orange-500", "to-yellow-500"]}

        />
        
        <GradientCard
          title="Portfolio Optimization"
          description={[
            "Utilized Python APIs to web scrape companies listed in the S&P 500.",
            "Formulated an optimization problem to maximize portfolio returns with constraints to reduce volatility.",
            "Employed Gurobi to solve the problem within a maximum allowable variance of 7%."
          ]}
          colors={["from-red-500", "via-orange-500", "to-yellow-500"]}

        />

        <GradientCard
          title="Apartment Database"
          description={[
            "Designed and implemented a relational database to simulate operations within an apartment complex.",
            "Created and executed SQL queries using MySQL to manage tenants, apartments, and maintenance records."
          ]}
          colors={["from-red-500", "via-orange-500", "to-yellow-500"]}

        />

        <GradientCard
          title="Runningback Evaluation"
          description={[
            "Worked with a group to make statistical observations on running back performance in the NFL based on age.",
            "Used permutation and parametric tests to analyze the difference in two means and the difference in two proportions."
          ]}
          colors={["from-red-500", "via-orange-500", "to-yellow-500"]}

        />
            </div>

      </div>
    </div>
  );
};

export default CardView;
