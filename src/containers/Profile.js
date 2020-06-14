import React from "react";
import { Form, Input, Select, Upload, message, Button, Skeleton } from "antd";
import { InboxOutlined, PlusOutlined, LoadingOutlined } from "@ant-design/icons";
import { connect } from "react-redux";
import Autocomplete from 'react-google-autocomplete';
import Hoc from "../hoc/hoc";

class Profile extends React.PureComponent {

  constructor(props) {
    super(props)
    this.state = this.initialState()
    this.handlePlaceSelect = this.handlePlaceSelect.bind(this)
    this.handleChange = this.handleChange.bind(this)
    this.autocomplete = null
  }

  initialState() {
    return {
      name: '',
    }
  }

  handleChange(event) {
    this.setState({[event.target.name]: event.target.value})
  }

  handlePlaceSelect() {
    let addressObject = this.autocomplete.getPlace()
    this.setState({
      name: addressObject.name,
    })
  }

  componentDidMount() {
  }

  componentWillReceiveProps(newProps) {
  }

  validateMobileNumber = (rule, value, callback) => {
    if(value.length !==10 ){
      callback("Invalid mobile number. Please enter 10 digit number");
    } else {
      callback();
    }
  }

  getBase64(img, callback) {
    const reader = new FileReader();
    reader.addEventListener('load', () => callback(reader.result));
    reader.readAsDataURL(img);
  }

  handleChange1 = info => {
    if (info.file.status === 'uploading') {
      this.setState({ loading: true });
      return;
    }
    if (info.file.status === 'done') {
      // Get this url from response in real world.
      this.getBase64(info.file.originFileObj, imageUrl =>
        this.setState({
          imageUrl,
          loading: false,
        }),
      );
    }
  };

  beforeUpload(file) {
    const isJpgOrPng = file.type === 'image/jpeg' || file.type === 'image/png';
    if (!isJpgOrPng) {
      message.error('You can only upload JPG/PNG file!');
    }
    const isLt2M = file.size / 1024 / 1024 < 2;
    if (!isLt2M) {
      message.error('Image must smaller than 2MB!');
    }
    return isJpgOrPng && isLt2M;
  }

  // onPlaceSelected = ( place ) => {
	// 	const address = place.formatted_address,
	// 	this.setState({
	// 		address: ( address ) ? address : '',
	// 	})
	// };


  render() {
    const normFile = e => {
      console.log('Upload event:', e);
      if (Array.isArray(e)) {
        return e;
      }
      return e && e.fileList;
    };

    const uploadButton = (
      <div>
        {this.state.loading ? <LoadingOutlined /> : <PlusOutlined />}
        <div className="ant-upload-text">Upload</div>
      </div>
    );
    const { imageUrl } = this.state;
    return (
      <Hoc>
        {this.props.loading ? (
          <Skeleton active />
        ) : (
          <Hoc>
            <div>
              <Form
                labelCol={{ span: 4 }}
                wrapperCol={{ span: 14 }}
                layout="horizontal"
              >
                <Form.Item name='firstname' label="First Name" rules ={[{ required: true, message: 'Please input your First name!'}]}>
                  <Input />
                </Form.Item>
                <Form.Item name='lastname' label="Last Name" rules ={[{ required: true, message: 'Please input your Last name!'}]}>
                  <Input />
                </Form.Item>
                <Form.Item name='shop_name' label="Shop Name" rules ={[{ required: true, message: 'Please input your Shop name!'}]}>
                  <Input />
                </Form.Item>
                <Form.Item name='phone' label="Phone Number" rules ={[{ required: true, message: 'Please input your phone number!'},{validator: this.validateMobileNumber}]}>
                  <Input />
                </Form.Item>
                <Form.Item name='address' label="Address" rules ={[{ required: true, message: 'Please input your Address!'}]}>
                  <Autocomplete
                    style={{width: '100%'}}
                    onPlaceSelected={(place) => {
                    console.log(place);
                    }}
                    types={['(regions)']}
                  />
                </Form.Item>
                <Form.Item name='landmark' label="Land Mark" rules ={[{ required: true, message: 'Please input your Land Mark!'}]}>
                  <Input />
                </Form.Item>
                <Form.Item name='pincode' label="Pin Code" rules ={[{ required: true, message: 'Please input your Pin Code!'}]}>
                  <Input />
                </Form.Item>
                <Form.Item name='bank_acc_no' label="Bank Acc No." rules ={[{ required: true, message: 'Please input your Bank Acc No.!'}]}>
                  <Input />
                </Form.Item>
                <Form.Item name='ifsc_code' label="IFSC Code" rules ={[{ required: true, message: 'Please input your IFSC Code!'}]}>
                  <Input />
                </Form.Item>
                <Form.Item name='transport_mode' label="Transport Mode" rules ={[{ required: true, message: 'Please input your Transport Mode!'}]}>
                  <Select>
                    <Select.Option value="P">Pickup</Select.Option>
                    <Select.Option value="D">Delivery</Select.Option>
                  </Select>
                </Form.Item>
                <Form.Item name='document_verification' label="Document Verification">
                  <Upload
                    name="avatar"
                    listType="picture-card"
                    className="avatar-uploader"
                    showUploadList={false}
                    action="https://www.mocky.io/v2/5cc8019d300000980a055e76"
                    beforeUpload={this.beforeUpload}
                    onChange={this.handleChange1}
                  >
                    {imageUrl ? <img src={imageUrl} alt="avatar" style={{ width: '100%' }} /> : uploadButton}
                  </Upload>
                </Form.Item>
                <Form.Item name='shop_image' label="Shop Image">
                  <Upload
                    name="avatar"
                    listType="picture-card"
                    className="avatar-uploader"
                    showUploadList={false}
                    action="https://www.mocky.io/v2/5cc8019d300000980a055e76"
                    beforeUpload={this.beforeUpload}
                    onChange={this.handleChange1}
                  >
                    {imageUrl ? <img src={imageUrl} alt="avatar" style={{ width: '100%' }} /> : uploadButton}
                  </Upload>
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
                <Form.Item>
                  <Button style={{ float: 'right' }}>Submit</Button>
                </Form.Item>
              </Form>
            </div>
          </Hoc>
        )}
      </Hoc>
    );
  }
}

const mapStateToProps = state => {
  return {
    token: state.auth.token,
    username: state.auth.username,
  };
};

const mapDispatchToProps = dispatch => {
  return {
  };
};

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(Profile);
