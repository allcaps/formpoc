import bootstrap from "bootstrap";
import axios from "axios";
import Cookies from 'js-cookie';
import form from './form';

axios.defaults.headers.post['X-CSRFToken'] = Cookies.get('csrftoken');
form();
