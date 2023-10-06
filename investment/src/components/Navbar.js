import React, { useState } from "react";
import { Link } from "react-router-dom";
import '../navbar.css'

function Navbar() {
  const [active, setActive] = useState(false); 
  const [icon, setIcon] = useState("nav__toggler");
<<<<<<< HEAD

  const navToggle = () => {
    if (active === "nav__menu") {
      setActive("nav__menu nav__active");
    } else setActive("nav__menu");

    if (icon === "nav__toggler") {
      setIcon("nav__toggler toggle");
    } else setIcon("nav__toggler");
  };

=======

  const navToggle = () => {
    setActive(!active); 
    setIcon(icon === "nav__toggler" ? "nav__toggler toggle" : "nav__toggler");
  };

  const navClass = active ? "nav__menu nav__active" : "nav__menu";

>>>>>>> 231d69d0ecf34e92c8df8f08afa0d8c5d909db42
  return (
    <nav className="nav">
      <Link to="/" className="nav__brand">
        Investment App
      </Link>
<<<<<<< HEAD
      <ul className={active}>
=======
      <ul className={navClass}>
>>>>>>> 231d69d0ecf34e92c8df8f08afa0d8c5d909db42
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
<<<<<<< HEAD
          <Link to="/losses" className="nav__link">
            Losses
          </Link>
        </li>
        <li className="nav__item">
          <Link to="/profits" className="nav__link">
            Profits
          </Link>
        </li>
=======
          <Link to="/profitloss" className="nav__link">
          Profits & Losses
          </Link>
        </li>
        
>>>>>>> 231d69d0ecf34e92c8df8f08afa0d8c5d909db42
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
