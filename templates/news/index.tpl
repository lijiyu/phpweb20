<h1>News<h1>

{if $news|@count == 0}
	<p>
		No news found
	</p>
{else}
	<ul>
		{foreach from=$news item=article}
			<li>{$article|escape}</li>
		{/foreach>
	</ul>
{/if}