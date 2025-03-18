import { useTheme } from '@/components/theme-provider';
import { useFetchKnowledgeList } from '@/hooks/knowledge-hooks';
import { IRetrievalNode } from '@/interfaces/database/flow';
import { UserOutlined } from '@ant-design/icons';
import { Handle, NodeProps, Position } from '@xyflow/react';
<<<<<<< HEAD
import { Avatar, Button, Flex } from 'antd';
import classNames from 'classnames';
import { get } from 'lodash';
import { useMemo, useState } from 'react';
=======
import { Avatar, Flex } from 'antd';
import classNames from 'classnames';
import { get } from 'lodash';
import { useMemo } from 'react';
>>>>>>> be730d39 (init commit)
import { LeftHandleStyle, RightHandleStyle } from './handle-icon';
import styles from './index.less';
import NodeHeader from './node-header';

export function RetrievalNode({
  id,
  data,
  isConnectable = true,
  selected,
}: NodeProps<IRetrievalNode>) {
  const knowledgeBaseIds: string[] = get(data, 'form.kb_ids', []);
  const { theme } = useTheme();
  const { list: knowledgeList } = useFetchKnowledgeList(true);
<<<<<<< HEAD
  const [showAllKnowledge, setShowAllKnowledge] = useState(false);
=======
>>>>>>> be730d39 (init commit)
  const knowledgeBases = useMemo(() => {
    return knowledgeBaseIds.map((x) => {
      const item = knowledgeList.find((y) => x === y.id);
      return {
        name: item?.name,
        avatar: item?.avatar,
        id: x,
      };
    });
  }, [knowledgeList, knowledgeBaseIds]);

<<<<<<< HEAD
  const displayedKnowledgeBases = showAllKnowledge
    ? knowledgeBases
    : knowledgeBases.slice(0, 3);
  function showAllItem(e: any) {
    e.stopPropagation(); // Prevent event from bubbling to parent
    setShowAllKnowledge(!showAllKnowledge);
  }
=======
>>>>>>> be730d39 (init commit)
  return (
    <section
      className={classNames(
        styles.logicNode,
        theme === 'dark' ? styles.dark : '',
        {
          [styles.selectedNode]: selected,
        },
      )}
    >
      <Handle
        id="c"
        type="source"
        position={Position.Left}
        isConnectable={isConnectable}
        className={styles.handle}
        style={LeftHandleStyle}
      ></Handle>
      <Handle
        type="source"
        position={Position.Right}
        isConnectable={isConnectable}
        className={styles.handle}
        style={RightHandleStyle}
        id="b"
      ></Handle>
      <NodeHeader
        id={id}
        name={data.name}
        label={data.label}
        className={classNames({
          [styles.nodeHeader]: knowledgeBaseIds.length > 0,
        })}
      ></NodeHeader>
      <Flex vertical gap={8}>
<<<<<<< HEAD
        {displayedKnowledgeBases.map((knowledge) => {
=======
        {knowledgeBases.map((knowledge) => {
>>>>>>> be730d39 (init commit)
          return (
            <div className={styles.nodeText} key={knowledge.id}>
              <Flex align={'center'} gap={6}>
                <Avatar
                  size={26}
                  icon={<UserOutlined />}
                  src={knowledge.avatar}
                />
                <Flex className={styles.knowledgeNodeName} flex={1}>
                  {knowledge.name}
                </Flex>
              </Flex>
            </div>
          );
        })}
<<<<<<< HEAD
        {knowledgeBases.length > 3 && (
          <div className={styles.nodeText}>
            <Button
              type="link"
              size="small"
              onClick={showAllItem}
              style={{
                padding: 0,
                height: 'auto',
                lineHeight: '1.5',
                textAlign: 'left',
              }}
            >
              {showAllKnowledge
                ? 'Hide'
                : `Show more ${knowledgeBases.length - 3} knowledge`}
            </Button>
          </div>
        )}
=======
>>>>>>> be730d39 (init commit)
      </Flex>
    </section>
  );
}
