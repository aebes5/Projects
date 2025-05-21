import React from 'react';
import HomeAnimation from './utils/HomeAnimation';
import 'css-doodle';

const Home = () => {
  return (
    <div style={styles.container}>
      <HomeAnimation />
      <h2 style={styles.name}>Andrew Ebert</h2>
    </div>
  );
}

const styles = {
  container: {
    display: 'flex',
    alignItems: 'center', 
    width: '90vw',
  },
  name: {
    fontSize: '80px',
    fontWeight: 'bold',
    color: "#FFFFFF",
  }
}

export default Home;
