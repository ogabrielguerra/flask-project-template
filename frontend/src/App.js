import React from 'react';
import './App.css';
import Search from './components/Search'

function App() {
  return (
      <div>
        <div className="header">
          <div className="container">
            <div className="row">
              <div className="col-md-12"><h3>Merchants Guide App</h3></div>
            </div>
          </div>
        </div>

        <div className="container">
          <div className="row mt-5">
            <div className="col-md-12">
                <Search/>
            </div>
          </div>
        </div>
      </div>
  );
}

export default App;
