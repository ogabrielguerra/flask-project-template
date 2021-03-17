import React from 'react'
import axios from "axios";

class Search extends React.Component{

    state = {
        showSearch : true,
        result : ""
    }

    constructor(props)  {
        super(props);
        this.sendQuery = this.sendQuery.bind(this);
        this.handleInput = this.handleInput.bind(this);
    }

    sendQuery(e){
        e.preventDefault();

        let value = this.refs.query.value;
        value = value.replace(/ /g,',')

        let iniUrl = `/mg-api/${value}`;

        axios.get(iniUrl)
            .then((response) => {
                console.log(response.data.value)
                this.setState(
                    {
                        showSearch : false,
                        result : response.data.value
                    }
                )
            })
    }

    handleInput(){
        if(this.refs.query.value !== "")
            this.refs.query.value = ""

        this.setState({result : ""})
    }

    render(){

        const RenderMe = ()=> {
            if (this.state.result !== "" && this.state.result !== "invalid query") {
                return (
                    <div>
                        <div className="col-12 mt-5">
                            <h2>{this.state.result} credits.</h2>
                        </div>
                    </div>
                )
            }else if(this.state.result === "invalid query"){
                return(
                    <div>
                        <div className="col-12 mt-5">
                            <h1>I have no idea what you are talking about.</h1>
                        </div>
                    </div>
                )
            }else{
                return (<div/>)
            }
        }

        return (
            <form onSubmit={this.sendQuery}>
            <div className="row">

                <div className="col-6">
                    <input ref="query" placeholder="Insert your Intergalactic query" onClick={this.handleInput} className="form-control form-control-lg"/>
                </div>
                <div className="col-6">
                    <button className="btn btn-primary btn-lg" onClick={this.sendQuery}>Convert</button>
                </div>

                <RenderMe/>
            </div>
            </form>
        )
    }

}

export default Search