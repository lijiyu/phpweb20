<?php


//require_once('Zend/Loader.php');
//Zend_Loader::registerAutoload();

require_once('Zend/Loader/Autoloader.php');
Zend_Loader_Autoloader::getInstance()->setFallbackAutoloader(true);

//config
$config = new Zend_Config_Ini('../settings.ini','development');
Zend_Registry::set('config', $config);

//create logger
$logger = new Zend_Log(new Zend_Log_Writer_Stream($config->logging->file));
Zend_Registry::set('logger', $logger);
$logger->debug('Test');

//connect mysql
$parms = array('host'=>$config->database->hostname,
               'username'=>$config->database->username,
               'password'=>$config->database->password,
               'dbname'=>$config->database->database);

$db = Zend_Db::factory($config->database->type,$parms);
Zend_Registry::set('db', $db);


//handle the user request
$controller = Zend_Controller_Front::getInstance();
$controller->setControllerDirectory($config->paths->base.'/include/Controllers');


//setup view render
$vr = new Zend_Controller_Action_Helper_ViewRenderer();
$vr->setView(new Templater());
$vr->setViewSuffix('tpl');
Zend_Controller_Action_HelperBroker::addHelper($vr);


$controller->dispatch();

?>


