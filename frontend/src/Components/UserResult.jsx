import React from "react";
import "../App.css";
import * as ReactDOM from "react-dom";

function Result(props) {
  if (props.warn) {
    return <div>Hello</div>;
  }
  return null;
}

class UserResult extends React.Component {
  constructor(props) {
    super(props);
    this.state = { showResult: true };
  }
  render() {
    return <div>hello</div>;
  }
}
export default UserResult;

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<UserResult />);

// class Page extends React.Component {
//   constructor(props) {
//     super(props);

//     this.handleToggleClick = this.handleToggleClick.bind(this);
//   }

//   handleToggleClick() {
//     this.setState(prevState => ({
//       showWarning: !prevState.showWarning
//     }));
//   }

//   render() {
//     return (
//       <div>
//         <WarningBanner warn={this.state.showWarning} />
//         <button onClick={this.handleToggleClick}>
//           {this.state.showWarning ? 'Hide' : 'Show'}
//         </button>
//       </div>
//     );
//   }
// }
