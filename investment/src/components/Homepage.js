// import React, { useState } from 'react'
// import '../App.css'
// import { Login } from './Login';
// import { SignUp } from './SignUp';

// function Homepage() {
//   const [currentForm, setCurrentForm] = useState('login');

//   const toggleForm = (formName) => {
//     setCurrentForm(formName);
//   }
//   return (
    
//        <div className="App">
//       {
//         currentForm === "login" ? <Login onFormSwitch={toggleForm} /> : <SignUp onFormSwitch={toggleForm} />
//       }
//     </div>
    
//   )
// }

// export default Homepage

import React, { useState } from 'react';
import '../App.css';
import { Login } from './Login';
import { SignUp } from './SignUp';

function Homepage() {
  const [currentForm, setCurrentForm] = useState('login');

  const toggleForm = (formName) => {
    setCurrentForm(formName);
  }

  return (
    <div className="App">
      <div className="auth-form-container">
        {currentForm === "login" ? (
          <div>
            <Login />
            <button className="link-btn" onClick={() => toggleForm('register')}>
              Don't have an account? Register here.
            </button>
          </div>
        ) : (
          <div>
            <SignUp />
            <button className="link-btn" onClick={() => toggleForm('login')}>
              Already have an account? Login here.
            </button>
          </div>
        )}
      </div>
    </div>
  );
}

export default Homepage;
