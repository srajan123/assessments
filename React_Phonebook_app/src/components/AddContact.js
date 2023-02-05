import React from "react";

class AddContact extends React.Component {
  state = {
    name: "",
    email: "",
    number: "",
    note: "",
  };

  add = (e) => {
    e.preventDefault();
    if (this.state.name === "" || this.state.email === "") {
      alert("ALl the fields are mandatory!");
      return;
    }
    this.props.addContactHandler(this.state);
    this.setState({ name: "", email: "", number: "", note: ""});
  };
  render() {
    return (

      <div className="main">
        <h2>Add Contact</h2>
        <form className="ui form" onSubmit={this.add}>

          <div className="field">
            <label>Name</label>
            <input
              type="text"
              name="name"
              placeholder="Name"
              value={this.state.name}
              onChange={(e) => this.setState({ name: e.target.value })}
            />
          </div>

          <div className="field">
            <label>Email</label>
            <input
              type="email"
              name="email"
              placeholder="Email"
              value={this.state.email}
              onChange={(e) => this.setState({ email: e.target.value })}
            />
          </div>

          <div className="field">
            <label>Contact number</label>
            <input
              type="tel"
              pattern="[789][0-9]{9}"
              name="number"
              placeholder="number"
              value={this.state.number}
              onChange={(e) => this.setState({ number: e.target.value })}
            />
          </div>

          <div className="field">
            <label>Note</label>
            <input
              type="text"
              name="note"
              placeholder="Note"
              value={this.state.note}
              onChange={(e) => this.setState({ note: e.target.value })}
            />
          </div>

          <button className="ui button green">Add</button>
        </form>
      </div>
    );
  }
}

export default AddContact;
