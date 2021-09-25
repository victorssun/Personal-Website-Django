let Modal = React.createClass({
    componentDidMount(){
        $(ReactDOM.findDOMNode(this)).modal('show');
        $(ReactDOM.findDOMNode(this)).on('hidden.bs.modal', this.props.handleHideModal);
    },
    render(){
        return (
          <div className="modal fade">
            <div className="modal-dialog">
              <div className="modal-content">
                <div className="modal-header">
                  <button type="button" className="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                  <h4 className="modal-title">Modal title</h4>
                </div>
                <div className="modal-body">
                  <p>One fine body&hellip;</p>
                </div>
                <div className="modal-footer">
                  <button type="button" className="btn btn-default" data-dismiss="modal">Close</button>
                  <button type="button" className="btn btn-primary">Save changes</button>
                </div>
              </div>
            </div>
          </div>
        )
    },
    propTypes:{
        handleHideModal: React.PropTypes.func.isRequired
    }
});



let App = React.createClass({
    getInitialState(){
        return {view: {showModal: false}}
    },
    handleHideModal(){
        this.setState({view: {showModal: false}})
    },
    handleShowModal(){
        this.setState({view: {showModal: true}})
    },
    render(){
    return(
        <div className="row">
            <button className="btn btn-default btn-block" onClick={this.handleShowModal}>Open Modal</button>
            {this.state.view.showModal ? <Modal handleHideModal={this.handleHideModal}/> : null}
        </div>
    );
  }
});

React.render(
   <App />,
    document.getElementById('container')
);