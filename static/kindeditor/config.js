/**
 * Created by WJ on 2018-05-28.
 */
KindEditor.ready(function(K) {
        // K.create('textarea[name=content]', {
        K.create('#id_content', {
            width: '70%',
            height: '600px',
            'uploadJson':'/admin/upload/kindeditor',
        });
});