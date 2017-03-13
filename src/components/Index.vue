<template>
  <div class="container">
  <h1>SDN List Search <span v-if='loading'>(loading most recent)</span></h1>
  <h1 v-if='error'>Error retrieving data</h1>
  <div class="input">
    <label>Enter a name:</label>
    <input type='text' v-model="search">
    <input type='checkbox' id='indCheckbox' v-model='showIndividuals'>
    <label for='indCheckbox'>Individuals</label>  
    <input type='checkbox' id='entityCheckbox' v-model='showEntities'>
    <label for='entityCheckbox'>Entities</label>
  </div>
  <div class="table" v-if='!loading && isInput'>
    <div id="ind-table" v-if='showIndividuals'>
      <h3>Individuals: {{ filteredIndividuals.length }}</h3>
      <table>
        <thead v-if='filteredIndividuals.length > 0'>
          <tr>
            <th class="ind-name">Name</th>
            <th class="ind-details">Details</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="individual in filteredIndividuals">
            <td>{{ individual.name }}</td>
            <td>{{ individual.details }}</td>
          </tr>
        </tbody>
      </table>
    </div>
    <div id="entity-table" v-if='showEntities'>
      <h3>Entities: {{ filteredEntities.length }}</h3>
      <table>
        <thead v-if='filteredEntities.length > 0'>
          <tr>
            <th class="entity-name">Entity Name</th>
            <th class="entity-details">Affiliation</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="entity in filteredEntities">
            <td>{{ entity.name }}</td>
            <td>{{ entity.details }}</td>
          </tr>
        </tbody>
      </table>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'index',
  data () {
    return {
      msg: 'LedgerX SDN Checker',
      individuals: [],
      entities: [],
      showIndividuals: true,
      showEntities: true,
      search: '',
      error: false,
      loading: true,
    }
  },
  methods: {
    getSDNIndividuals: function() {
      this.$http.get('http://127.0.0.1:5000/individuals').then(response => {
        this.individuals = response.body;
        }, response => {
          this.error = true;
        }
      );
    },
    getSDNEntities: function() {
      this.$http.get('http://127.0.0.1:5000/entities').then(response => {
        this.entities = response.body;
        this.loading = false;
        }, response => {
          this.error = true;
        }
      );
    }
  },
  computed: {
    filteredIndividuals: function() {
      return this.individuals.filter(individual => {
        return individual.name.indexOf(this.search.toUpperCase()) > -1
      });
    },
    filteredEntities: function() {
      return this.entities.filter(entity => {
        return entity.name.indexOf(this.search.toUpperCase()) > -1
      });
    },
    isInput: function() {
      return (this.search.length > 1);
    },
  },
  created: function() {
    this.getSDNIndividuals();
    this.getSDNEntities();
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

th, td {
  padding-top: 12px;
  padding-bottom: 12px;
  text-align: left;
  border-bottom: 1px solid #ddd;
}

tr {
  height: 25px;
  vertical-align: top;
  line-height: 1.35em;
}

.ind-name {
  width: 30%;
}
.ind-details {
  width: 70%;
}

.entity-name {
  width: 70%;
}

.entity-details {
  width: 30%;
}

.input {
  padding-bottom: 50px;
}

</style>
