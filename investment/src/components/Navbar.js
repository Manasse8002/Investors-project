// import React, { useState } from "react";
// import "../navbar.css";

// function Navbar() {
//   const [active, setActive] = useState("nav__menu");
//   const [icon, setIcon] = useState("nav__toggler");
//   const navToggle = () => {
//     if (active === "nav__menu") {
//       setActive("nav__menu nav__active");
//     } else setActive("nav__menu");

//     // Icon Toggler
//     if (icon === "nav__toggler") {
//       setIcon("nav__toggler toggle");
//     } else setIcon("nav__toggler");
//   };
//   return (
//       <nav className="nav">
//         <a href="/" className="nav__brand">
//           investment app
//         </a>
//         <ul className={active}>
//           <li className="nav__item">
//             <a href="/" className="nav__link">
//               Home
//             </a>
//           </li>
//           <li className="nav__item">
//             <a href="/actions" className="nav__link">
//               Actions
//             </a>
//           </li>
//           <li className="nav__item">
//             <a href="/about" className="nav__link">
//               About
//             </a>
//           </li>
//         </ul>
//         <div onClick={navToggle} className={icon}>
//           <div className="line1"></div>
//           <div className="line2"></div>
//           <div className="line3"></div>
//         </div>
//       </nav>
//   );
// }

// export default Navbar;

import React, { useState } from "react";
// import "./navbar.css";
import { Link } from "react-router-dom";
import '../navbar.css'

function Navbar() {
  const [active, setActive] = useState("nav__menu");
  const [icon, setIcon] = useState("nav__toggler");

  const navToggle = () => {
    if (active === "nav__menu") {
      setActive("nav__menu nav__active");
    } else setActive("nav__menu");

    if (icon === "nav__toggler") {
      setIcon("nav__toggler toggle");
    } else setIcon("nav__toggler");
  };

  return (
    <nav className="nav">
      <Link to="/" className="nav__brand">
        Investment App
      </Link>
      <ul className={active}>
        <li className="nav__item">
          <Link to="/" className="nav__link">
            Home
          </Link>
        </li>
        <li className="nav__item">
          <Link to="/about" className="nav__link">
            About
          </Link>
        </li>
        <li className="nav__item">
          <Link to="/investments" className="nav__link">
            Investments
          </Link>
        </li>
        <li className="nav__item">
          <Link to="/investors" className="nav__link">
            Investors
          </Link>
        </li>
        <li className="nav__item">
          <Link to="/losses" className="nav__link">
            Losses
          </Link>
        </li>
        <li className="nav__item">
          <Link to="/profits" className="nav__link">
            Profits
          </Link>
        </li>
      </ul>
      <div onClick={navToggle} className={icon}>
        <div className="line1"></div>
        <div className="line2"></div>
        <div className="line3"></div>
      </div>
    </nav>
  );
}

export default Navbar;
