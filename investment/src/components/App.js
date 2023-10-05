import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Home from './Home'; 
import InvestorsTable from './InvestorsTable';
import InvestmentsTable from './InvestmentsTable';
import LossesTable from './LossTable';
import ProfitsTable from './ProfitTable';

function App() {
  return (
    <Router> 
      <div>
        <main>
          <Switch>
            <Route exact path="/">
              <Home />
            </Route>
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
