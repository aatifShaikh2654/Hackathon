import React, { useContext } from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import './global.css';
import App from './App';
import State from './context/state/State';
import User from './context/user/User';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <State>
      <User>
        <App />
      </User>
    </State>
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals