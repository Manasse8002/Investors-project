import React, { useState } from 'react'
import '../App.css'
import { Login } from '../components2/Login'
import { SignUp } from '../components2/SignUp';


function Homepage() {
  const [currentForm, setCurrentForm] = useState('login');

  const toggleForm = (formName) => {
    setCurrentForm(formName);
  }
  return (
    
       <div className="App">
      {
        currentForm === "login" ? <Login onFormSwitch={toggleForm} /> : <SignUp onFormSwitch={toggleForm} />
      }
    </div>
    
  )
}

export default Homepage