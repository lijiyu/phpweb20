<?php
class NewsController extends Zend_Controller_Action
{
	public function indexAction(){
		require_once('Smarty/Smarty.class.php');
		
		$article = array(
		    'New Article1',
		    '新闻20',
		    '其他新闻');
		
		$smarty = new Smarty();
		$smarty->template_dir = $config->paths->template;
		$smarty->compile_dir = $config->paths->data.'/temp/template_c';
        $smarty->assign('news',$article);
        $smarty->display('news/index.tpl');
	}
	public function displayAction(){
		echo 'News article details';
	}
}