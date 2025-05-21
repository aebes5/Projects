import React from 'react'
import { Link } from 'react-router-dom';
import { FaEnvelope, FaLinkedin, FaGithub, FaGit } from 'react-icons/fa';
import image from './newton-fractal-example-plot-npe1.jpg';

const Header = () => {
  return (
    <header style = {styles.header}>
        <div style = {styles.leftSection}>
          <img src = {image} style = {styles.imageStyle} />  
          <h1 style = {styles.name}>Denver, CO</h1> 
        </div>
        <nav style = {styles.nav}>
            <ul style = {styles.navList}>
                <li><Link to="/" className="text-white hover:text-gray-400">Home</Link></li>
                <li><Link to="/About" className = "text-white hover:text-gray-400">About</Link></li>
                <li><Link to="/Projects" className = "text-white hover:text-gray-400">Projects</Link></li>
                <li><Link to="/Skills" className = "text-white hover:text-gray-400">Skills</Link></li>    
            </ul>
        </nav>
        <div style = {styles.socialIcons}>
            <a href = "mailto:andrew.ebert12@yahoo.com">
                <FaEnvelope size={24} style = {styles.socialIcon}/>
            </a>
            <a href = "https://www.linkedin.com/in/andrew-e-ebert">
                <FaLinkedin size = {24} style = {styles.socialIcon}/>
            </a>
            <a href = "https://github.com/aebes5">
                <FaGithub size = {24} style = {styles.socialIcon}/>    
            </a>
        </div>
    </header>
  );
};

const styles = {
    header: {
      display: 'flex',
      justifyContent: 'space-between',
      alignItems: 'center',
      padding: '20px 40px',
      backgroundColor: '#000',
      color: '#fff',
    },
    leftSection: {
      display: 'flex',
      alignItems: 'center',
      gap: '1rem',
      flex: 1, // Align left
    },
    name: {
      margin: 0,
      display: 'flex',
      fontSize: '20px',
    },
    nav: {
      flex: 1,
      display: 'flex',
      justifyContent: 'center', // Center the nav items
    },
    navList: {
      display: 'flex',
      justifyContent: 'center',
      listStyleType: 'none',
      margin: 0,
      padding: 0,
      gap: '30px',
      fontSize: '20px',
    },
    socialIcons: {
      flex: 1,
      display: 'flex',
      justifyContent: 'flex-end',
      gap: '25px',
      alignItems: 'center',
    },
    socialIcon: {
        color: '#fff',
    },
    imageStyle: {
      width: '28px', 
      height: '28px', 
      borderRadius: '50%', 
    },
};

export default Header