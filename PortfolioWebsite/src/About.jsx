import React from 'react'
import GradientCard from './utils/GradientCard'

const About = () => {
  return (
    <div>
    <h_title>About Me</h_title>
    <h_desc>A list of education, contact information, and work history.</h_desc>
    <div className="flex items-center justify-center">
    <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6 p-4">
    <GradientCard
        title="Education"
        description={["I am a senior at the University of Colorado-Denver studying Computer Science and Applied Mathematics.", "I will graduate in May of 2025.", 
          "My upcoming/current courses include Data Science, Deep Learning, Machine Learning, Data Mining, Software Engineering, and Math Clinic."]}
        colors={["from-indigo-500", "via-magenta-500", "to-pink-500"]}
      />
      <GradientCard
        title="Contact"
        description={[
        <span>Email: <a href="mailto:andrew.ebert12@yahoo.com" className="text-blue-300 underline">andrew.ebert12@yahoo.com</a></span>,
          <span>LinkedIn: <a href="https://www.linkedin.com/in/andrew-e-ebert" target="_blank" rel="noopener noreferrer" className="text-blue-300 underline">www.linkedin.com/in/andrew-e-ebert</a></span>,
          <span>Phone Number: <a href="tel:+17206279163" className="text-blue-300 underline">(720) 627-9163</a></span>,
          <span>GitHub: <a href="https://github.com/aebes5" target="_blank" rel="noopener noreferrer" className="text-blue-300 underline">https://github.com/aebes5</a></span>,
          <span>Resume: <a href="/Ebert_Andrew_Portfolio_Resume.pdf" target="_blank" rel="noopener noreferrer" className="text-blue-300 underline">View Resume</a></span>
        ]}
        colors={["from-indigo-500", "via-magenta-500", "to-pink-500"]}
      />
      <GradientCard
        title="Student Researcher"
        description={["CU Denver(May 2023 - July 2024)", "Automated the execution of 18 jobs on supercomputers using JSON.",
          "Compiled code, primarily using Intel compilers and Intel MKL, to run high-performance computing jobs and optimize performance.", 
          "Developed machine learning models using Python to classify four classes of electronic/atomic transitions.",
          "Analyzed and visualized complex datasets, collaborating with a team to create scripts using Matplotlib and Pandas.",
          "Participated in a group research presentation on high-performance computing at CU Denver's 2023 RACAS."
        ]}
        colors={["from-indigo-500", "via-magenta-500", "to-pink-500"]}
      />
      <GradientCard
        title="Construction Laborer"
        description={["Accell Construction(August 2021 - May 2023)",
          "Applied a strong attention to detail and effective time management to efficiently complete tasks while ensuring the client's specifications were met.", 
          "Collaborated with a team, balancing individual tasks with collective goals of ensuring projects were completed on time."
        ]}
        colors={["from-indigo-500", "via-magenta-500", "to-pink-500"]}
      />
      </div>
      </div>
      </div>
  )
}

export default About