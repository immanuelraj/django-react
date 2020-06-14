import React from "react";
import { connect } from "react-redux";
import { NavLink } from "react-router-dom";
import { Button, Input, Table, Skeleton } from "antd";
import { PlusCircleOutlined, SearchOutlined } from '@ant-design/icons';
import * as actions from "../store/actions/products";
import Hoc from "../hoc/hoc";

class ProductList extends React.PureComponent {
  componentDidMount() {
    if (this.props.token !== undefined && this.props.token !== null) {
      this.props.getProducts(this.props.token);
      console.log(this.props.products)
    }
  }

  componentWillReceiveProps(newProps) {
    if (newProps.token !== this.props.token) {
      if (newProps.token !== undefined && newProps.token !== null) {
        this.props.getProducts(newProps.token);
        console.log(this.props.products)
      }
    }
  }

  renderItem(item) {
    return (
      <NavLink to={`/product/${item.id}`}></NavLink>
    );
  }

  render() {
    const columns = [
      {
        title: 'Name',
        dataIndex: 'name',
        key: 'name',
        render: (text, record) => (
          <NavLink to={`product/${record.ext_id}`}>{text}</NavLink>
        )
      },
      {
        title: 'Category',
        dataIndex: 'category',
        key: 'category',
      },
      {
        title: 'Price',
        dataIndex: 'price',
        key: 'price',
      },
      {
        title: 'Availability',
        dataIndex: 'availability',
        key: 'availability',
      },
    ];
    return (
      <Hoc>
        {this.props.loading ? (
          <Skeleton active />
        ) : (
          <Hoc>
            <Input
              placeholder="input search text"
              onSearch={value => console.log(value)}
              suffix={<SearchOutlined />}
              style={{ width: 400 }}
            />
            <Button type="secondary" style={{ marginBottom: '10px', marginLeft: '20%' }} href={'/product/create'}>
            <PlusCircleOutlined /> Add Item
            </Button>
            <Table dataSource={this.props.products} columns={columns} bordered />
          </Hoc>
        )}
      </Hoc>
    )
  }
}

const mapStateToProps = state => {
  return {
    token: state.auth.token,
    products: state.products.products,
    loading: state.products.loading
  };
};

const mapDispatchToProps = dispatch => {
  return {
    getProducts: token => dispatch(actions.getProducts(token))
  };
};

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(ProductList);
