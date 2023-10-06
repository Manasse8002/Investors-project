import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Navbar from './components/Navbar';
import Homepage from './components/Homepage';
import About from './components/About';
import InvestmentsTable from './components/InvestmentsTable';
import InvestorsTable from './components/InvestorsTable';
import ProfitLossTable from './components/ProfitLossTable';

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
            <Route path="/profitloss" component={ProfitLossTable} />
            
          </Switch>
        </main>
      </div>
    </Router>
  );
}

export default App;
