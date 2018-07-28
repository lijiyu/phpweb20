<?php
//自定义控制器
class CustomController extends Zend_Controller_Action
{
	public $db;
	
	public function init() {
	    $this->db = Zend_Registry::get('db');
	}
}