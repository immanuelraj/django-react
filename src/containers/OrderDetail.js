import React from "react";
import { connect } from "react-redux";
import { Card, Skeleton, message } from "antd";
import { getOrderDetail } from "../store/actions/orders";
import Hoc from "../hoc/hoc";

class OrderDetail extends React.Component {
  state = {
    usersAnswers: {}
  };

  componentDidMount() {
    if (this.props.token !== undefined && this.props.token !== null) {
      this.props.getASNTSDetail(this.props.token, this.props.match.params.id);
    }
  }

  componentWillReceiveProps(newProps) {
    if (newProps.token !== this.props.token) {
      if (newProps.token !== undefined && newProps.token !== null) {
        this.props.getASNTSDetail(newProps.token, this.props.match.params.id);
      }
    }
  }

  onChange = (e, qId) => {
    const { usersAnswers } = this.state;
    usersAnswers[qId] = e.target.value;
    this.setState({ usersAnswers });
  };

  handleSubmit() {
    message.success("Submitting your assignment!");
  }

  render() {
    const { currentAssignment } = this.props;
    const { title } = currentAssignment;
    return (
      <Hoc>
        {Object.keys(currentAssignment).length > 0 ? (
          <Hoc>
            {this.props.loading ? (
              <Skeleton active />
            ) : (
              <Card title={title}>
              </Card>
            )}
          </Hoc>
        ) : null}
      </Hoc>
    );
  }
}

const mapStateToProps = state => {
  return {
    token: state.auth.token,
    currentAssignment: state.assignments.currentAssignment,
    loading: state.assignments.loading,
    username: state.auth.username
  };
};

const mapDispatchToProps = dispatch => {
  return {
    getOrderDetail: (token, id) => dispatch(getOrderDetail(token, id)),
  };
};

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(OrderDetail);