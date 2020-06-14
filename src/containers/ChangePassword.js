import React from "react";
import { Form, Input, Button, Row, Col, Card } from "antd";
import { LockOutlined } from "@ant-design/icons";
import { connect } from "react-redux";
import * as actions from "../store/actions/auth";

const FormItem = Form.Item;

class ChangePassword extends React.Component {
  state = {
    confirmDirty: false,
  };
  handleSubmit = (values) => {
    const product = {
      old_password: values.old_password,
      new_password1: values.new_password1,
      new_password2: values.new_password2,
    };
    if (this.props.token !== undefined && this.props.token !== null) {
      this.props.onAuthPasswordReset(this.props.token, product);
    }
  };

  handleConfirmBlur = (e) => {
    const value = e.target.value;
    this.setState({ confirmDirty: this.state.confirmDirty || !!value });
  };

  render() {
    return (
      <Row
        type="flex"
        justify="center"
        align="middle"
        style={{ minHeight: "100vh" }}
      >
        <Col span={8}>
          <Card>
            <Form onFinish={this.handleSubmit}>
            <FormItem
                name="old_password"
                rules={[
                  { required: true, message: "Please input your old password!" },
                ]}
                hasFeedback
              >
                <Input
                  prefix={<LockOutlined className="site-form-item-icon" />}
                  type="password"
                  placeholder="Old Password"
                />
              </FormItem>
              <FormItem
                name="new_password1"
                rules={[
                  { required: true, message: "Please input your new password!" },
                ]}
                hasFeedback
              >
                <Input
                  prefix={<LockOutlined className="site-form-item-icon" />}
                  type="password"
                  placeholder="New Password"
                />
              </FormItem>
              <FormItem
                name="new_password2"
                rules={[
                  {
                    required: true,
                    message: 'Please confirm your new password!',
                  },
                  ({ getFieldValue }) => ({
                    validator(rule, value) {
                      if (!value || getFieldValue('new_password1') === value) {
                        return Promise.resolve();
                      }
                      return Promise.reject('The two passwords that you entered do not match!');
                    },
                  }),
                ]}
                hasFeedback
              >
                <Input
                  prefix={<LockOutlined className="site-form-item-icon" />}
                  type="password"
                  placeholder="Confirm New Password"
                  onBlur={this.handleConfirmBlur}
                />
              </FormItem>
              <FormItem>
                <Button
                  type="primary"
                  htmlType="submit"
                  style={{ marginRight: "10px" }}
                >
                  Change Password
                </Button>
              </FormItem>
            </Form>
          </Card>
        </Col>
      </Row>
    );
  }
}

const mapStateToProps = (state) => {
  return {
    token: state.auth.token,
    loading: state.auth.loading,
    error: state.auth.error,
  };
};

const mapDispatchToProps = (dispatch) => {
  return {
    onAuthPasswordReset: (oldpassword, password1, password2) =>
      dispatch(
        actions.authPasswordReset( oldpassword, password1, password2)
      ),
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(ChangePassword);
