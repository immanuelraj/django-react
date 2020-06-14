import React from "react";
import { connect } from "react-redux";
import { Form, Input, Upload, Button, Select, InputNumber } from "antd";
import { InboxOutlined } from "@ant-design/icons";
import { createProduct } from "../store/actions/products";
import * as actions from "../store/actions/category";


const FormItem = Form.Item;

class ProductCreate extends React.Component {

  componentDidMount() {
    if (this.props.token !== undefined && this.props.token !== null) {
      this.props.getCategories(this.props.token);
      console.log(this.props.categories)
    }
  }

  componentWillReceiveProps(newProps) {
    if (newProps.token !== this.props.token) {
      if (newProps.token !== undefined && newProps.token !== null) {
        this.props.getCategories(newProps.token);
        console.log(this.props.categories)
      }
    }
  }

  handleSubmit = values => {
    const product = {
      // vender: this.props.username,
      name: values.name,
      category: values.category,
      availability: values.availability,
      price: values.price,
      image: 'rose-blue-flower-rose-blooms-67636_gbDtIN3.jpeg'
    };
    this.props.createProduct(this.props.token, product);
  };

  render() {
    const normFile = e => {
      console.log('Upload event:', e);
      if (Array.isArray(e)) {
        return e;
      }
      return e && e.fileList;
    };
    return (
      <Form onFinish={this.handleSubmit} labelCol={{ span: 4 }} wrapperCol={{ span: 14 }} layout="horizontal">
        <Form.Item name = 'name' validateTrigger ={["onChange", "onBlur"]} label='Name' rules ={[
            {
              required: true,
              message: "Please input a name"
            }
          ]}>
          <Input placeholder="Add a Product Name" />
        </Form.Item>
        <Form.Item name='category' label="Category" rules ={[{ required: true, message: 'Please input Category!'}]}>
          <Select placeholder="Select the Product Category">
            <Select.Option value="1">Pickup</Select.Option>
            <Select.Option value="2">Delivery</Select.Option>
          </Select>
        </Form.Item>
        <Form.Item name='availability' label="Availability" rules ={[{ required: true, message: 'Please input Availability!'}]}>
          <Select placeholder="Select the Product Availability">s
            <Select.Option value="A">Available</Select.Option>
            <Select.Option value="N"> Not Available</Select.Option>
          </Select>
        </Form.Item>
        <Form.Item name='price' label="Price (INR)" rules ={[{ required: true, message: 'Please input Non Decimal Price!'}]}>
          <InputNumber step={0.1} placeholder="199" style={{ width: '100%' }}/>
        </Form.Item>
        <Form.Item label="Dragger">
          <Form.Item name="dragger" valuePropName="fileList" getValueFromEvent={normFile} noStyle>
            <Upload.Dragger name="files" action="/upload.do">
              <p className="ant-upload-drag-icon">
                <InboxOutlined />
              </p>
              <p className="ant-upload-text">Click or drag file to this area to upload</p>
              <p className="ant-upload-hint">Support for a single or bulk upload.</p>
            </Upload.Dragger>
          </Form.Item>
        </Form.Item>
        <Form.Item></Form.Item>
        <FormItem>
          <Button type="primary" htmlType="submit" style={{ float: 'left', marginLeft:'450px' }}>
            Add Item
          </Button>
        </FormItem>
      </Form>
    );
  }
}

const mapStateToProps = state => {
  return {
    token: state.auth.token,
    username: state.auth.username,
    loading: state.products.loading
  };
};

const mapDispatchToProps = dispatch => {
  return {
    createProduct: (token, product) => dispatch(createProduct(token, product)),
    getCategories: token => dispatch(actions.getCategories(token))
  };
};

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(ProductCreate);
