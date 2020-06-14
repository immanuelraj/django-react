import React from "react";
import { connect } from "react-redux";
import { Card, message } from "antd";
import { getProductsDetail } from "../store/actions/products";


class ProductDetail extends React.Component {
  state = {
    usersAnswers: {}
  };

  componentDidMount() {
    if (this.props.token !== undefined && this.props.token !== null) {
      this.props.getProductsDetail(this.props.token, this.props.match.params.id);
    }
  }

  componentWillReceiveProps(newProps) {
    if (newProps.token !== this.props.token) {
      if (newProps.token !== undefined && newProps.token !== null) {
        this.props.getProductsDetail(newProps.token, this.props.match.params.id);
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
    const { usersAnswers } = this.state;
    const asnt = {
      username: this.props.username,
      asntId: this.props.currentAssignment.id,
      answers: usersAnswers
    };
    this.props.createGradedASNT(this.props.token, asnt);
  }

  render() {
    return (
      <div className="site-card-border-less-wrapper">
        <Card title="Card title" bordered={false} style={{ width: 300 }}>
          <p>Card content</p>
          <p>Card content</p>
          <p>Card content</p>
        </Card>
      </div>
      // <Hoc>
      //   <h2>HI</h2>
      //   {Object.keys(currentProduct).length > 0 ? (
      //     <Hoc>
      //       <h2>HI</h2>
      //       {this.props.loading ? (
      //         <Skeleton active />
      //       ) : (
      //         <Card title={title}>
      //           <h2>HI</h2>
      //         </Card>
      //       )}
      //     </Hoc>
      //   ) : null}
      // </Hoc>
    );
  }
}

const mapStateToProps = state => {
  return {
    token: state.auth.token,
    currentProduct: state.products.currentProduct,
    loading: state.products.loading,
    username: state.auth.username
  };
};

const mapDispatchToProps = dispatch => {
  return {
    getProductsDetail: (token, id) => dispatch(getProductsDetail(token, id)),
  };
};

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(ProductDetail);
