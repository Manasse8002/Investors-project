import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Navbar from './components/Navbar';
import Homepage from './components/Homepage';
import About from './components/About';
import InvestorsTable from './components/InvestorsTable';
import InvestmentsTable from './components/InvestmentsTable';
import LossesTable from './components/LossTable'
import ProfitTable from './components/ProfitTable';

function App() {
  return (
    <Router>
      <div>
        <main>
          <Navbar />
          <Switch>
            <Route path="/" exact component={Homepage} />
            <Route path="/about" component={About} />
            <Route path="/investments" component={InvestmentsTable} />
            <Route path="/investors" component={InvestorsTable} />
            <Route path="/losses" component={LossesTable} />
            <Route path="/profits" component={ProfitTable} />
          </Switch>
        </main>
      </div>
    </Router>
  );
}

export default App;
