import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Navbar from './components/Navbar';
import Homepage from './components/Homepage';
import About from './components/About';
<<<<<<< HEAD
import InvestorsTable from './components/InvestorsTable';
import InvestmentsTable from './components/InvestmentsTable';
import LossesTable from './components/LossTable'
import ProfitTable from './components/ProfitTable';
=======
import InvestmentsTable from './components/InvestmentsTable';
import InvestorsTable from './components/InvestorsTable';
import ProfitLossTable from './components/ProfitLossTable';
>>>>>>> 231d69d0ecf34e92c8df8f08afa0d8c5d909db42

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
<<<<<<< HEAD
            <Route path="/losses" component={LossesTable} />
            <Route path="/profits" component={ProfitTable} />
=======
            <Route path="/profitloss" component={ProfitLossTable} />
            
>>>>>>> 231d69d0ecf34e92c8df8f08afa0d8c5d909db42
          </Switch>
        </main>
      </div>
    </Router>
  );
}

<<<<<<< HEAD
export default App;
=======
export default App;
>>>>>>> 231d69d0ecf34e92c8df8f08afa0d8c5d909db42
