// import React from 'react';
// import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
// import Navbar from './components/Navbar';
// import Home from './components/Homepage';
// import About from './components/About';
// // import Actions from './components/Actions';
// import InvestorsTable from './components/InvestorsTable';
// import InvestmentsTable from './components/InvestmentsTable';
// import LossesTable from './components/LossTable';
// import ProfitsTable from './components/ProfitTable';

// function App() {
//   return (
//     <Router> 
//       <div>
//         <main>
//           <Navbar />
//           <Switch>
//             <Route path="/" element={<Home />} />
//             <Route path="/about" element={<About />} />
//             {/* <Route path='/actions' element={<Actions />} /> */}
//             <Route exact path="/InvestmentsTable/:id">
//               <InvestmentsTable /> 
//             </Route>
//             <Route exact path="/InvestorsTable/:id">
//               <InvestorsTable />
//             </Route>
//             <Route exact path="/LossTables/:id">
//               <LossesTable /> 
//             </Route>
//             <Route exact path="/ProfitTable/:id">
//               <ProfitsTable /> 
//             </Route>
//           </Switch>
//         </main>
//       </div>
//     </Router>
//   );
// }

// export default App;
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
