import React from "react";
import { connect } from "react-redux";
import { Button, Input, Menu, Table, Skeleton, Dropdown } from "antd";
import { DownOutlined, UserOutlined, SearchOutlined } from '@ant-design/icons';
import * as actions from "../store/actions/orders";
import Hoc from "../hoc/hoc";

class OrderDetailList extends React.PureComponent {
  componentDidMount() {
    if (this.props.token !== undefined && this.props.token !== null) {
      this.props.getOrders(this.props.token);
    }
  }

  componentWillReceiveProps(newProps) {
    if (newProps.token !== this.props.token) {
      if (newProps.token !== undefined && newProps.token !== null) {
        this.props.getOrders(newProps.token);
      }
    }
  }

  render() {

    const menu = (
      <Menu>
        <Menu.Item key="1" icon={<UserOutlined />}>
          Open
        </Menu.Item>
        <Menu.Item key="2" icon={<UserOutlined />}>
          Completed
        </Menu.Item>
        <Menu.Item key="3" icon={<UserOutlined />}>
          In Progress
        </Menu.Item>
      </Menu>
    );

    const dataSource = [
      {
        key: '1',
        name: 'sdasdasd',
        price: 32,
        category: '10 Downing Street',
        availability: 'Yes',
      },
      {
        key: '2',
        name: 'dsdsadsa',
        price: 42,
        category: '10 Downing Street',
        availability: 'No'
      },
    ];
    
    const columns = [
      {
        title: 'Customer Name',
        dataIndex: 'name',
        key: 'name',
      },
      {
        title: 'Address',
        dataIndex: 'address',
        key: 'address',
      },
      {
        title: 'Status',
        dataIndex: 'status',
        key: 'status',
      },
      {
        title: 'Delivery/Pickup Time',
        dataIndex: 'delivery_time',
        key: 'delivery_time',
      },
      {
        title: 'Product Count',
        dataIndex: 'product_count',
        key: 'product_count',
      },
      {
        title: 'Total Price',
        dataIndex: 'total_price',
        key: 'total_price',
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
              style={{ width: 400, marginBottom: '10px' }}
            />
            <Dropdown overlay={menu} placement="bottomCenter" >
              <Button style={{ marginLeft: '10%' }}>
                Status <DownOutlined />
              </Button>
            </Dropdown>
            <Table dataSource={dataSource} columns={columns} />
          </Hoc>
        )}
      </Hoc>
    )
  }
}

const mapStateToProps = state => {
  return {
    token: state.auth.token,
    orders: state.orders.orders,
    loading: state.orders.loading
  };
};

const mapDispatchToProps = dispatch => {
  return {
    getOrders: token => dispatch(actions.getOrders(token))
  };
};

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(OrderDetailList);