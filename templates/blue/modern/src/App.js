import React, {Component} from 'react';
import logo from './images/bookapp.jpg';
import './App.css';

class App extends Component {
    render() {
        return (
            <div className="container">
                <a href="http://127.0.0.1:8000">Home</a>&nbsp;<a href="">Books</a>&nbsp;<a href="">Bookmarks</a>
                <br/><br/><br/>
                <div className="row">
                    <div className="col-lg-6 centerize">
                        <img className="rounded-circle" height="300" width="500" src={logo} alt="Bookapp"/>
                    </div>
                </div>
                <br/>
                <form method="get" action="">
                    <div className="row">
                        <div className="col-lg-6 centerize">
                            <div className="form-group">
                                <input name="q" type="text" className="form-control"
                                       placeholder="Book name, author or isbn13 number"/>
                            </div>
                        </div>
                    </div>
                    <div className="row">
                        <div className="col-lg-3">&nbsp;</div>
                        <div className="col-lg-3">
                            <div className="form-group">
                                <button className="btn btn-light form-control" type="submit">Search Bookapp</button>
                            </div>
                        </div>
                        <div className="col-lg-3">
                            <div className="form-group">
                                <button className="btn btn-light form-control" type="submit">I feel lucky myself
                                </button>
                            </div>
                        </div>
                    </div>
                </form>
            </div>
        );
    }
}

export default App;
