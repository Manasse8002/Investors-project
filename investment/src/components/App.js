import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Navbar from './components/Navbar';
import Home from './components/Homepage';
import About from './components/About';
import Actions from './components/Actions';
import InvestorsTable from './InvestorsTable';
import InvestmentsTable from './InvestmentsTable';
import LossesTable from './LossTable';
import ProfitsTable from './ProfitTable';

function App() {
  return (
    <Router> 
      <div>
        <main>
          <Navbar />
          <Switch>
            <Route path="/" element={<Home />} />
            <Route path="/about" element={<About />} />
            <Route path='/actions' element={<Actions />} />
            <Route exact path="/InvestmentsTable/:id">
              <InvestmentsTable /> 
            </Route>
            <Route exact path="/InvestorsTable/:id">
              <InvestorsTable />
            </Route>
            <Route exact path="/LossTables/:id">
              <LossesTable /> 
            </Route>
            <Route exact path="/ProfitTable/:id">
              <ProfitsTable /> 
            </Route>
          </Switch>
        </main>
      </div>
    </Router>
  );
}

export default App;
