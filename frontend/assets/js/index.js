var React = require('react');
var ReactDOM = require('react-dom');

var EntryList = React.createClass({
    loadEntriesFromServer: function(){
        $.ajax({
            url: this.props.url,
            datatype: 'json',
            cache: false,
            success: function(data) {
                this.setState({data: data});
            }.bind(this)
        });
    },

    getInitialState: function() {
        return {data: []};
    },

    componentDidMount: function() {
        this.loadEntriesFromServer();
        setInterval(this.loadEntriesFromServer,
                    this.props.pollInterval);
    },
    render: function() {
        if (this.state.data) {
            console.log(this.state.data);
            var entryNodes = this.state.data.map(function(entry){
                return <li key={entry.id}> {entry.text} </li>;
            });
        }
        return (
            <div>
                <h1>Hello React!</h1>
                <ul>
                    {entryNodes}
                </ul>
            </div>
        );
    }
});

ReactDOM.render(<EntryList url='/api/entry/' pollInterval={1000} />,
    document.getElementById('container'));
