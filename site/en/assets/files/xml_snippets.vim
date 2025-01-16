" liquibase snippets
"  * use lhelp snippet for help
"  author: Marek Wywial <marek@marekwywial.name>
"  
if !exists('loaded_snippet') || &cp
    finish
endif

let st = g:snip_start_tag
let et = g:snip_end_tag
let cd = g:snip_elem_delim

function! SelectTrueFalse()
    let st = g:snip_start_tag
    let et = g:snip_end_tag
    let cd = g:snip_elem_delim
    let dt = inputlist(['Select value:',
                \ '1. autoIncrement: true',
                \ '2. autoIncrement: false'])
    let dts = { 1: " autoIncrement=\"true\"",
            \   2: "" }
    return dts[dt]
endfunction

function! SelectColumnType()
    let st = g:snip_start_tag
    let et = g:snip_end_tag
    let cd = g:snip_elem_delim
    let cdt = inputlist(['Select value:',
                \ '1. INT',
                \ '2. DECIMAL',
                \ '3. TEXT',
                \ '4. VARCHAR',
                \ '5. BOOLEAN',
                \ '6. DATETIME'])
    let cdts = { 1: 'type="INT" valueNumeric="'.st.et.'" defaultValueNumeric="'.st.et.'"',
            \   2: 'type="DECIMAL('.st.et.','.st.et.')" valueNumeric="'.st.et.'" defaultValueNumeric="'.st.et.'"',
            \   3: 'type="TEXT" value="'.st.et.'" defaultValue="'.st.et.'"',
            \   4: 'type="VARCHAR('.st.et.')" value="'.st.et.'" defaultValue="'.st.et.'"',
            \   5: 'type="BOOLEAN" valueBoolean="'.st.et.'" defaultValueBoolean="'.st.et.'"',
            \   6: 'type="DATETIME" valueDate="'.st.et.'" defaultValueDate="'.st.et.'"'
            \   }
    return cdts[cdt]
endfunction

exec 'Snippet laddcolumn <addColumn tableName="'.st.et.'"><CR>'.st.et.'<CR></addColumn><CR>'.st.et
exec 'Snippet laddfk <addForeignKeyConstraint constraintName="'.st.et.'"<CR>baseTableName="'.st.et.'" baseColumnNames="'.st.et.'"<CR>referencedTableName="'.st.et.'" referencedColumnNames="'.st.et.'"<CR>onDelete="'.st.et.'"<CR>/><CR>'.st.et
exec 'Snippet ladduniq <addUniqueConstraint tableName="'.st.et.'" constraintName="'.st.et.'" columnNames="'.st.et.'" /><CR>'.st.et
exec "Snippet lchangelog <?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?><CR> <databaseChangeLog xmlns=\"http://www.liquibase.org/xml/ns/dbchangelog/1.8\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"http://www.liquibase.org/xml/ns/dbchangelog/1.8 http://www.liquibase.org/xml/ns/dbchangelog/dbchangelog-1.8.xsd\"><CR>".st.et
exec "Snippet lchangeset <changeSet author=\"".st.et."\" id=\"".st.et."\"><CR>".st.et."</changeSet><CR>".st.et
exec 'Snippet lcolumn <column``SelectTrueFalse()`` name="'.st.et.'" ``SelectColumnType()``><CR><constraints nullable="'.st.et.'" primaryKey="'.st.et.'"/><CR></column><CR>'.st.et
exec 'Snippet lcomment <comment>'.st.et.'</comment><CR>'.st.et
exec 'Snippet lcreateindex <createIndex indexName="'.st.et.'" tableName="'.st.et.'" unique="'.st.et.'"><CR>'.st.et
exec "Snippet lcreatetable <createTable tableName=\"".st.et."\"><CR>".st.et."</createTable><CR>".st.et
exec 'Snippet ldropcolumn <dropColumn tableName="'.st.et.'" columnName="'.st.et.'"/>'.st.et

exec 'Snippet lhelp <!-- lhelp laddcolumn laddfk ladduniq lchangelog lchangeset lcolumn lcomment lcreateindex lcreatetable ldropcolumn --><CR>'.st.et
